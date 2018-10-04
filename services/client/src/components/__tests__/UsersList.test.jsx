import React from 'react';
import renderer from 'react-test-renderer';
import { shallow } from 'enzyme';
import UsersList from '../UsersList';

const users = [
    {
        'active': true,
        'email': 'theo@huxtable.com',
        'username': 'theo',
        'id': 1,

    },
    {
        'active': true,
        'email': 'red@hat.com',
        'username': 'rudolph',
        'id': 2,
    }
];

test('UsersList renders properly', () => {
    const wrapper = shallow(<UsersList users={users}/>);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.children).toBe('theo');
});

test('UsersList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
});
