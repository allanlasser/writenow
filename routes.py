#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/groups/')
def group_list():
    return render_template('group/list.html')

@routes.route('/groups/create')
def group_create():
    return render_template('group/create.html')

@routes.route('/groups/<int:group_id>/')
def group_detail(group_id):
    return render_template('group/detail.html')

@routes.route('/groups/<int:group_id>/join')
def group_join(group_id):
    return 'Oh, so you want to join group %d?' % group_id

@routes.route('/groups/<int:group_id>/leave')
def group_leave(group_id):
    return 'Oh, so you want to leave group %d?' % group_id

@routes.route('/prompts/')
def prompt_list():
    return render_template('prompt/list.html')

@routes.route('/prompts/<int:prompt_id>/')
def prompt_detail(prompt_id):
    return 'This is the page for prompt %d.' % prompt_id

@routes.route('/prompts/<int:prompt_id>/<int:response_id>')
def response_detail(prompt_id, response_id):
    return 'This is the page for response %d to prompt %d.' % (
        response_id,
        prompt_id
    )
