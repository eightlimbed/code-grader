# Tests the Users service

import json
import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


# Helper function to add users for GET all users test
def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):

    def test_users(self):
        '''Ensure the /ping route works successfully'''
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_a_user(self):
        '''Ensure a new user can be added to the db'''
        with self.client:
            response = self.client.post('/users',
                                        data=json.dumps({
                                            'username': 'theo',
                                            'email': 'theo@huxtable.com'
                                        }),
                                        content_type='application/json',
                                        )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('theo@huxtable.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        '''Ensure error is thrown if the JSON object is empty.'''
        with self.client:
            response = self.client.post(
                    '/users',
                    data=json.dumps({}),
                    content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

        def test_add_user_invalid_json_keys(self):
            '''Ensure error is thrown if the JSON object does not have a
            username key.'''
            with self.client:
                response = self.client.post(
                        '/users',
                        data=json.dumps({'email': 'a@bc.com'}),
                        content_type='application/json',
                )
                data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 400)
                self.assertIn('Invalid payload', data['message'])
                self.assertIn('fail', data['status'])

        def test_add_user_duplicate_email(self):
            '''Ensure error is thrown if email already exists.'''
            with self.client:
                response = self.client.post(
                        '/users',
                        data=json.dumps({
                            'name': 'Henry',
                            'email': 'theo@huxtable.com'
                        }),
                        content_type='application/json',
                )
                data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 400)
                self.assertIn('Sorry. That email already exists.',
                              data['message'])
                self.assertIn('fail', data['status'])

    def test_single_user(self):
        '''Ensure get single user behaves correctly.'''
        user = add_user('theo', 'theo@huxtable.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('theo', data['data']['username'])
            self.assertIn('theo@huxtable.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        '''Ensure error is thrown if an id is not provided.'''
        with self.client:
            response = self.client.get('/users/xxx')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        '''Ensure error is thrown if the id does not exist.'''
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        '''Ensure get all users behaves correctly.'''
        add_user('lee', 'lee@gmail.com')
        add_user('thom', 'thom@yorke.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('lee', data['data']['users'][0]['username'])
            self.assertIn('lee@gmail.com', data['data']['users'][0]['email'])
            self.assertIn('thom', data['data']['users'][1]['username'])
            self.assertIn('thom@yorke.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        '''Ensure the main route behaves correctly when no users have been added
        to the database.'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Users', response.data)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_users(self):
        '''Ensure the main route behaves correctly when users have been added to
        the database.'''
        add_user('Tim', 'tim@duncan.com')
        add_user('Gregg', 'gregg@ourcinema.org')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'Tim', response.data)
            self.assertIn(b'Gregg', response.data)

    def test_main_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username='donniedarko', email='donnie@darko.com'),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'donniedarko', response.data)


if __name__ == '__main__':
    unittest.main()
