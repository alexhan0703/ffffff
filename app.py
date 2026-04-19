1 import os
    2 from flask import Flask, render_template, request, jsonify
    3 from flask_sqlalchemy import SQLAlchemy
    4 from dotenv import load_dotenv
    5
    6 load_dotenv()
    7
    8 app = Flask(__name__)
    9
   10 # [수정] DATABASE_URL의 'postgres://'를 'postgresql://'로 변환 (SQLAlchemy 호환성)
   11 database_url = os.getenv('DATABASE_URL', 'sqlite:///science_dict.db')
   12 if database_url.startswith("postgres://"):
   13     database_url = database_url.replace("postgres://", "postgresql://", 1)
   14
   15 app.config['SQLALCHEMY_DATABASE_URI'] = database_url
   16 app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   17
   18 db = SQLAlchemy(app)
   19
   20 class ScienceTerm(db.Model):
   21     id = db.Column(db.Integer, primary_key=True)
   22     term = db.Column(db.String(100), unique=True, nullable=False)
   23     definition = db.Column(db.Text, nullable=False)
   24     category = db.Column(db.String(50))
   25
   26     def to_dict(self):
   27         return {
   28             'id': self.id,
   29             'term': self.term,
   30             'definition': self.definition,
   31             'category': self.category
   32         }
   33
   34 # [수정] Gunicorn 실행 시에도 테이블이 자동 생성되도록 블록 밖으로 이동
   35 with app.app_context():
   36     db.create_all()
   37
   38 @app.route('/')
   39 def index():
   40     return render_template('index.html')
   41
   42 @app.route('/api/search')
   43 def search():
   44     query = request.args.get('q', '')
   45     if len(query) < 2:
   46         return jsonify([])
   47
   48     results = ScienceTerm.query.filter(ScienceTerm.term.ilike(f'%{query}%')).all()
   49     return jsonify([r.to_dict() for r in results])
   50
   51 @app.route('/api/term/<int:term_id>')
   52 def get_term(term_id):
   53     term = ScienceTerm.query.get_or_404(term_id)
   54     return jsonify(term.to_dict())
