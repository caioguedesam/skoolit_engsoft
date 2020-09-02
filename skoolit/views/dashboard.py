from flask import render_template, redirect, url_for, request, Blueprint, flash, jsonify

#local imports

dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/')
def bla():
	return jsonify({'bla': 'bla'})