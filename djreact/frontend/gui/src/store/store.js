import { createStore, compose, applyMiddleware } from 'redux'
import {reducer} from './reducers/auth';

import thunk from 'redux-thunk'

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

export const store = createStore(reducer, composeEnhances(
        applyMiddleware(thunk)
    ));