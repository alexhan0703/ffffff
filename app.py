import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# [수정] DATABASE_URL의 'postgres://'를 'postgresql://'로 변환 (SQLAlchemy 호환성)
database_url = os.getenv('DATABASE_URL', 'sqlite:///science_dict.db')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ScienceTerm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(100), unique=True, nullable=False)
    definition = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'term': self.term,
            'definition': self.definition,
            'category': self.category
        }

# [수정] Gunicorn 실행 시에도 테이블이 자동 생성되도록 설정
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    if len(query) < 2:
        return jsonify([])
    
    results = ScienceTerm.query.filter(ScienceTerm.term.ilike(f'%{query}%')).all()
    return jsonify([r.to_dict() for r in results])

@app.route('/api/term/<int:term_id>')
def get_term(term_id):
    term = ScienceTerm.query.get_or_404(term_id)
    return jsonify(term.to_dict())

if __name__ == '__main__':
    # 로컬 실행 시에는 5000번 포트 사용
    app.run(debug=True)
