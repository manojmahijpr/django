import axios from "axios";

export function postForm(post, updateState) {
    axios.post('http://127.0.0.1:8000/api/', {
        title: post.title,
        content: post.content
    })
    .then(res => {
        var article = {
            id: res.data.id,
            title: res.data.title,
            content: res.data.content
        }
        updateState(article)
    })
    .catch(err => console.error(err))
}

export function putForm(post, articleId, updateState) {
    axios.put(`http://127.0.0.1:8000/api/${articleId}`, {
        title: post.title,
        content: post.content
    })
    .then(res => {
        var article = {
            id: res.data.id,
            title: res.data.title,
            content: res.data.content
        }
        updateState(article)
    })
    .catch(err => console.error(err))    
}