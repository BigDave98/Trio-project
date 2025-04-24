from flask import Blueprint, jsonify, render_template
from app.mailchimp.mailchimp_SDK.retrieve_members import retrieve_contacts
from app.mailchimp.mailchimp_SDK.add_members import add_members

bp = Blueprint("main", __name__)

@bp.route("/contacts/sync", methods=["GET"])
def sync_contacts():  
    return retrieve_contacts() 

@bp.route("/contacts/add", methods=["POST"])
def post_new_contacts():
    result = add_members()
    return jsonify(result)

@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")