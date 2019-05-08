import React from 'react'
import { Link, withRouter } from 'react-router-dom';
import { Layout, Menu, Breadcrumb } from 'antd';

import * as actions from '../store/actions/auth'
import {connect} from 'react-redux'

const { Header, Content, Footer } = Layout;


class CustomLayout extends React.PureComponent {


    handleLogout = () => {
        this.props.logout();
        this.props.history.push('/login/')
    }

    render() {
        return(
            <Layout className="layout" >
                <Header>
                    <div className="logo" />
                    <Menu
                        theme="dark"
                        mode="horizontal"
                        defaultSelectedKeys={['2']}
                        style={{ lineHeight: '64px' }}
                    >
                        
                        {
                            this.props.isAuthenticated
                                ?
                                <Menu.Item key="1" onClick={this.handleLogout}>
                                    Logout
                                </Menu.Item>
                                :
                                <Menu.Item key="2" >
                                    <Link to="/login/">Login</Link>
                                </Menu.Item>
                        }
                        {
                            this.props.isAuthenticated
                            ?   <Menu.Item key="2">
                                    <Link to="/">Posts</Link>
                                </Menu.Item>
                            :   null
                        }
                        
                    </Menu>
                </Header>

                <Content style={{ padding: '0 50px' }}>
                    <Breadcrumb style={{ margin: '16px 0' }}>
                        <Breadcrumb.Item><Link to="/">Home</Link></Breadcrumb.Item>
                        <Breadcrumb.Item><Link to="/">List</Link></Breadcrumb.Item>
                    </Breadcrumb>
                    <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                        {
                            this.props.children
                            //console.log(this.props)
                            
                            //React.cloneElement(this.props.children, {...this.props})
                        }
                        
                    </div>
                </Content>

                <Footer style={{ textAlign: 'center' }}>
                    Ant Design ©2018 Created by Ant UED
                </Footer>
                
            </Layout>
        )
    }
}

const mapStateToProps = state => {
    return {
        loading: state.loading
    }
}

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.logout())
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(CustomLayout))