from flask import Flask, Blueprint
from flask_restful import Api

# from csd.resource import score_resume

csd_bp = Blueprint('csd',__name__)
api=Api(csd_bp)

# api.add_resource(score_resume,'/v1/csd/score/resume/<string:app_mode>')