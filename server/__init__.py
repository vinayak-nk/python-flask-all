from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
 

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video missing', required=True)
video_put_args.add_argument('views', type=int, help='Views of the video missing', required=True)
video_put_args.add_argument('likes', type=int, help='Likes on the video missing', required=True)

videos = {}


class Video(Resource):
  def get(self, video_id):
    if video_id in videos:
      return videos[video_id]
    else:
      abort(404, message='video id is not valid.......')
  
  def post(self, video_id):
    if video_id in videos:
      abort(409, message='video already exists')
    args = video_put_args.parse_args()
    videos[video_id] = args
    return videos[video_id], 201
  
  def delete(self, video_id):
    if video_id not in videos:
      abort(404, message='video does not exists')
    del videos[video_id]
    return '', 204
    
    
api.add_resource(Video, '/video/<int:video_id>')