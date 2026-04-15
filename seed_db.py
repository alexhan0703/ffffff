from app import db, ScienceTerm, app

def seed():
    terms = [
        {"term": "광합성", "category": "생물", "definition": "식물이 빛 에너지를 이용하여 이산화탄소와 물로부터 유기물을 합성하는 과정입니다."},
        {"term": "블랙홀", "category": "천문", "definition": "중력이 너무 강해 빛조차 빠져나갈 수 없는 시공간의 영역입니다."},
        {"term": "상대성 이론", "category": "물리", "definition": "알베르트 아인슈타인이 제안한 시간과 공간에 대한 물리 이론입니다."},
        {"term": "주기율표", "category": "화학", "definition": "원소를 원자 번호 순서대로 배열하여 성질의 주기성을 나타낸 표입니다."},
        {"term": "세포", "category": "생물", "definition": "생물체의 구조적, 기능적 기본 단위입니다."},
        {"term": "빅뱅", "category": "천문", "definition": "우주가 거대한 폭발로부터 시작되었다는 우주론적 모델입니다."},
        {"term": "엔트로피", "category": "물리", "definition": "계의 무질서도를 나타내는 물리량입니다."},
        {"term": "이온 결합", "category": "화학", "definition": "양이온과 음이온 사이의 정전기적 인력에 의해 형성되는 화학 결합입니다."}
    ]

    with app.app_context():
        db.create_all()
        for t in terms:
            if not ScienceTerm.query.filter_by(term=t['term']).first():
                new_term = ScienceTerm(**t)
                db.session.add(new_term)
        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    seed()
