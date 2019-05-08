import React, { Component } from 'react'

import {
    Form, Input, Button,
} from 'antd';

import {postForm, putForm} from '../actions/formActions'

class CustomForm extends Component {

    handleFormSubmit = (event, requestType, updateState, articleId) => {
        event.preventDefault();

        const title = event.target.elements.title.value
        const content = event.target.elements.content.value
        

        switch (requestType) {
            case 'post':
                postForm({
                    title,
                    content
                }, updateState);
                
                break;
            case 'put':
                putForm({
                        title,
                        content
                    },
                    articleId, updateState);
                break;
            default:
                break;
        }
        
    }



    render() {
        const { requestType, btnText , updateState, articleId} = this.props;
        return (
            <div>
                <Form onSubmit={(event)=> this.handleFormSubmit(event, requestType, updateState, articleId)}>
                    <Form.Item label="Title">
                        <Input name="title" placeholder="Enter Title here..." />
                    </Form.Item>
                    <Form.Item label="Content">
                        <Input name="content" placeholder="Enter some Content Here" />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit">{btnText}</Button>
                    </Form.Item>
                </Form>
            </div>
        );
    }
}

export default CustomForm;