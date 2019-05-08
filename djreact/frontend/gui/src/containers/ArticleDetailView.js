import React, { Component } from 'react'
import axios from 'axios'

import {connect} from 'react-redux'

import {Card, Button} from 'antd';
import CustomForm from '../components/Form';

class ArticleDetail extends Component {

    state = {
        article: {}
    }

    fetchArticle = () => {

        const articleId = this.props.match.params.articleId;

        axios.get(`http://127.0.0.1:8000/api/${articleId}`)
            .then((res) => {
                this.setState({ article: res.data });
            })
    }

    updateState = (article) => {
        this.setState({article});
        
    }

    componentDidMount() {
    
        const {isAuthenticated} =  this.props;
        if(isAuthenticated)
          this.fetchArticle();
        else 
          this.props.history.push('/login/')
        
    }
    
    handleDelete = (event) => {
        event.preventDefault();
        const articleId = this.props.match.params.articleId;
        axios.delete(`http://127.0.0.1:8000/api/${articleId}`)

        this.props.history.push('/')
    }

    render() {
        const articleId = this.props.match.params.articleId;
        return (
            <div>
                <Card title={this.state.article.title}>
                    <p>{this.state.article.content}</p>
                </Card>
                <CustomForm 
                    requestType='put'
                    articleId={articleId}
                    btnText={'Update'}
                    updateState={this.updateState}
                />
                <form onSubmit={this.handleDelete}>
                    <Button type="danger" htmlType="submit">Delete</Button>
                </form>
            </div>
        )
    }
}

const mapStateToProps = state => {
    
    return {
      isAuthenticated: state.token !== null ? true : false
    }
}

export default connect(mapStateToProps)(ArticleDetail);