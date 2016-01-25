#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/groups/')
def group_list():
    return render_template('group/list.html')

@app.route('/groups/create')
def group_create():
    return render_template('group/create.html')

@app.route('/groups/<int:group_id>/')
def group_detail(group_id):
    return render_template('group/detail.html')

@app.route('/groups/<int:group_id>/join')
def group_join(group_id):
    return 'Oh, so you want to join group %d?' % group_id

@app.route('/groups/<int:group_id>/leave')
def group_leave(group_id):
    return 'Oh, so you want to leave group %d?' % group_id

@app.route('/prompts/')
def prompt_list():
    return render_template('prompt/list.html')

@app.route('/prompts/<int:prompt_id>/')
def prompt_detail(prompt_id):
    return 'This is the page for prompt %d.' % prompt_id

@app.route('/prompts/<int:prompt_id>/<int:response_id>')
def response_detail(prompt_id, response_id):
    return 'This is the page for response %d to prompt %d.' % (
        response_id,
        prompt_id
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
