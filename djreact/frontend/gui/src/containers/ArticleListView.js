import React, { Component } from 'react'
import axios from 'axios'

import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom'

import Articles from '../components/Articles'
import CustomForm from '../components/Form';


class ArticleList extends Component {

  state = {
    articles: [],
    isAuthenticated: false
  }

  fetchArticles = ()=> {
    axios.get('http://127.0.0.1:8000/api/')
      .then((res) => {
        this.setState(
          {
            articles: res.data
          });
      })
  }

  updateState = (article) => {
    this.setState({
      articles: [...this.state.articles, article]
    })
  }

  componentDidMount() {

    if(localStorage.getItem('token')) {
      this.fetchArticles();
      this.setState({
        isAuthenticated: true
      });
    } 
  }

  componentWillUnmount() {
    this.setState({
      isAuthenticated: false
    });
  }

  render() {
    
    if(!localStorage.getItem('token')) {
      return <Redirect to="/login/" />
    }
    

    return (
      <div>
        <Articles data={this.state.articles}/>
        <br/>
        <h2>Create An Article</h2>
        <CustomForm 
          requestType='post'
          articleId={null}
          btnText='Create'
          updateState={this.updateState}
        />
      </div>
    )
  }
}


export default ArticleList