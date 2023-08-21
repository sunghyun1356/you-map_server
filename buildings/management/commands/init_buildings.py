from django.core.management.base import BaseCommand
from buildings.models import Building, Purpose, BuildingPurpose

class Command(BaseCommand):
    help = 'Initialize Buildings, Purposes'
    Buildings = [  
        {
            'name': '본관',
            'nickname': 'A',
            'latitude': 126.94007819205449,
            'longitude': 37.5510975386403
        },  
        {
            'name': '게페르트 남덕우 경제관',
            'nickname': 'GN',
            'latitude': 126.93987503840462,
            'longitude': 37.550417181702485
        },     
        {
            'name': '삼성 가브리엘관',
            'nickname': 'GA',
            'latitude': 126.93907595886981,
            'longitude': 37.551966488951756
        },
        {
            'name': '금호아시아나 바오로 경영관',
            'nickname': 'PA',
            'latitude': 126.93893992936553,
            'longitude': 37.5522457280733
        },     
        {
            'name': '토마스 모어관',
            'nickname': 'T',
            'latitude': 126.93826676658172,
            'longitude': 37.55201562355056
        },                        
        {
            'name': '마태오관',
            'nickname': 'MA',
            'latitude': 126.93921117873163,
            'longitude': 37.55268285204712
        },
        {
            'name': '메리홀',
            'nickname': 'M',
            'latitude': 126.93950021881795,
            'longitude': 37.55211537177174
        },
        {
            'name': '성이냐시오관',
            'nickname': 'I',
            'latitude': 126.94031508057311,
            'longitude': 37.55205271661622
        },
        {
            'name': '엠마오관',
            'nickname': 'E',
            'latitude': 126.94096638736507,
            'longitude': 37.55130521562026
        },
        {
            'name': '로욜라 도서관',
            'nickname': None,
            'latitude': 126.94174143078158,
            'longitude': 37.55149931516709
        },
        {
            'name': '최양업관',
            'nickname': 'CY',
            'latitude': 126.94227366121561,
            'longitude': 37.55105358247631
        },
        {
            'name': '다산관',
            'nickname': 'D',
            'latitude': 126.9432461463778,
            'longitude': 37.552040646855424
        },  
        {
            'name': '곤자가 플라자',
            'nickname': 'GP',
            'latitude': 126.94310553546391,
            'longitude': 37.55092334149706
        },
        {
            'name': '떼이야르관',
            'nickname': 'TE',
            'latitude': 126.94354156955775,
            'longitude': 37.550468546670245
        }, 
        {
            'name': '정하상관',
            'nickname': 'J',
            'latitude': 126.94305510067625,
            'longitude': 37.550279103420905
        },
        {
            'name': '포스코 프란치스코관',
            'nickname': 'F',
            'latitude': 126.94272691731523,
            'longitude': 37.55028344968517
        },
        {
            'name': '리치별관',
            'nickname': 'RA',
            'latitude':  126.94213292037642,
            'longitude': 37.55012548536896
        },
        {
            'name': '아담샬관',
            'nickname': 'AS',
            'latitude': 126.94181622225581,
            'longitude': 37.54991359512531
        },
        {
            'name': '리치과학관',
            'nickname': 'R',
            'latitude': 126.94126741121882,
            'longitude': 37.54986376850998
        },
        {
            'name': '김대건관',
            'nickname': 'K',
            'latitude': 126.9400903128349,
            'longitude': 37.55009293173118
        },
        {
            'name': '벨라르미노학사',
            'nickname': None,
            'latitude': 126.94013919165332,
            'longitude': 37.54911312074815 #여기까지
        },
        {
            'name': '서강빌딩',
            'nickname': None,
            'latitude': 126.9393722611631,
            'longitude': 37.54941681643926
        },
        {
            'name': '아루페관',
            'nickname': 'AR',
            'latitude': 126.93875511830862,
            'longitude': 37.54990303708855
        },
        {
            'name': '체육관',
            'nickname': None,
            'latitude': 126.93914833341303,
            'longitude': 37.549943785312536
        },
        {
            'name': '베르크만스 우정원',
            'nickname': 'BW',
            'latitude': 126.93909981128094,
            'longitude': 37.55046859181515
        },
    ]
    
    Purposes = [
        {
            'name': '휴게',
            'glyph': None,
        },
        {
            'name': '공부',
            'glyph': None,
        },
        {
            'name': '팀플',
            'glyph': None,
        },
        {
            'name': '경로',
            'glyph': None,
        },
        {
            'name': '기타',
            'glyph': None,
        },
    ]

    BuidlingPurposes = [
        {
            'building' : 1, # 본관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 1, # 본관
            'purpose' : 4 # 경로
        },
        {
            'building' : 1, # 본관
            'purpose' : 5 # 기타
        },
        {
            'building' : 2, # 게페르트 남덕우 경제관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 2, # 게페르트 남덕우 경제관
            'purpose' : 2 # 공부
        },
        {
            'building' : 2, # 게페르트 남덕우 경제관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 2, # 게페르트 남덕우 경제관
            'purpose' : 4 # 경로
        },
        {
            'building' : 2, # 게페르트 남덕우 경제관
            'purpose' : 5 # 기타
        },
        {
            'building' : 3, # 삼성 가브리엘관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 3, # 삼성 가브리엘관
            'purpose' : 2 # 공부
        },
        {
            'building' : 3, # 삼성 가브리엘관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 3, # 삼성 가브리엘관
            'purpose' : 4 # 경로
        },
        {
            'building' : 3, # 삼성 가브리엘관
            'purpose' : 5 # 기타
        },
        {
            'building' : 4, # 금호아시아나 바오로 경영관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 4, # 금호아시아나 바오로 경영관
            'purpose' : 2 # 공부
        },
        {
            'building' : 4, # 금호아시아나 바오로 경영관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 4, # 금호아시아나 바오로 경영관
            'purpose' : 4 # 경로
        },
        {
            'building' : 4, # 금호아시아나 바오로 경영관
            'purpose' : 5 # 기타
        },
        {
            'building' : 5, # '토마스 모어관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 5, # '토마스 모어관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 5, # '토마스 모어관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 5, # '토마스 모어관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 5, # '토마스 모어관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 6, # '마태오관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 6, # '마태오관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 6, # '마태오관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 6, # '마태오관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 6, # '마태오관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 7, # '메리홀'
            'purpose' : 4 # 경로
        },
        {
            'building' : 7, # '메리홀'
            'purpose' : 5 # 기타
        },
        {
            'building' : 8, # '성이냐시오관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 8, # '성이냐시오관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 8, # '성이냐시오관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 8, # '성이냐시오관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 8, # '성이냐시오관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 9, # '엠마오관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 9, # '엠마오관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 9, # '엠마오관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 9, # '엠마오관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 9, # '엠마오관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 10, # '로욜라 도서관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 10, # '로욜라 도서관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 10, # '로욜라 도서관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 10, # '로욜라 도서관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 10, # '로욜라 도서관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 11, #최양업관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 11, #최양업관
            'purpose' : 2 # 공부
        },
        {
            'building' : 11, #최양업관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 11, #최양업관
            'purpose' : 4 # 경로
        },
        {
            'building' : 11, #최양업관
            'purpose' : 5 # 기타
        },
        {
            'building' : 12, # 다산관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 12, # 다산관
            'purpose' : 2 # 공부
        },
        {
            'building' : 12, # 다산관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 12, # 다산관
            'purpose' : 4 # 경로
        },
        {
            'building' : 12, # 다산관
            'purpose' : 5 # 기타
        },
        {
            'building' : 13, # '곤자가 플라자'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 13, # '곤자가 플라자'
            'purpose' : 4 # 경로
        },
        {
            'building' : 13, # '곤자가 플라자'
            'purpose' : 5 # 기타
        },
        {
            'building' : 14, # 떼이야르관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 14, # 떼이야르관
            'purpose' : 2 # 공부
        },
        {
            'building' : 14, # 떼이야르관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 14, # 떼이야르관
            'purpose' : 4 # 경로
        },
        {
            'building' : 14, # 떼이야르관
            'purpose' : 5 # 기타
        },
        {
            'building' : 15, # 정하상관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 15, # 정하상관
            'purpose' : 2 # 공부
        },
        {
            'building' : 15, # 정하상관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 15, # 정하상관
            'purpose' : 4 # 경로
        },
        {
            'building' : 15, # 정하상관
            'purpose' : 5 # 기타
        },
        {
            'building' : 16, # '포스코 프란치스코관'
            'purpose' : 1 # 휴게
        },
        {
            'building' : 16, # '포스코 프란치스코관'
            'purpose' : 2 # 공부
        },
        {
            'building' : 16, # '포스코 프란치스코관'
            'purpose' : 3 # 팀플
        },
        {
            'building' : 16, # '포스코 프란치스코관'
            'purpose' : 4 # 경로
        },
        {
            'building' : 16, # '포스코 프란치스코관'
            'purpose' : 5 # 기타
        },
        {
            'building' : 17, # 리치별관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 17, # 리치별관
            'purpose' : 2 # 공부
        },
        {
            'building' : 17, # 리치별관
            'purpose' : 4 # 경로
        },
        {
            'building' : 17, # 리치별관
            'purpose' : 5 # 기타
        },{
            'building' : 18, # 아담샬관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 18, # 아담샬관
            'purpose' : 2 # 공부
        },
        {
            'building' : 18, # 아담샬관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 18, # 아담샬관
            'purpose' : 4 # 경로
        },
        {
            'building' : 18, # 아담샬관
            'purpose' : 5 # 기타
        },
        {
            'building' : 19, # 리치과학관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 19, # 리치과학관
            'purpose' : 2 # 공부
        },
        {
            'building' : 19, # 리치과학관
            'purpose' : 4 # 경로
        },
        {
            'building' : 19, # 리치과학관
            'purpose' : 5 # 기타
        },
        {
            'building' : 20, # 김대건관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 20, # 김대건관
            'purpose' : 2 # 공부
        },
        {
            'building' : 20, # 김대건관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 20, # 김대건관
            'purpose' : 4 # 경로
        },
        {
            'building' : 20, # 김대건관
            'purpose' : 5 # 기타
        },
        {
            'building' : 21, # 벨라르미노학사
            'purpose' : 1 # 휴게
        },
        {
            'building' : 21, # 벨라르미노학사
            'purpose' : 2 # 공부
        },
        {
            'building' : 21, # 벨라르미노학사
            'purpose' : 3 # 팀플
        },
        {
            'building' : 21, # 벨라르미노학사
            'purpose' : 4 # 경로
        },
        {
            'building' : 21, # 벨라르미노학사
            'purpose' : 5 # 기타
        },
        {
            'building' : 22, # 서강빌딩
            'purpose' : 1 # 휴게
        },
        {
            'building' : 22, # 서강빌딩
            'purpose' : 2 # 공부
        },
        {
            'building' : 22, # 서강빌딩
            'purpose' : 3 # 팀플
        },
        {
            'building' : 22, # 서강빌딩
            'purpose' : 4 # 경로
        },
        {
            'building' : 22, # 서강빌딩
            'purpose' : 5 # 기타
        },
        {
            'building' : 23, # 아루페관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 23, # 아루페관
            'purpose' : 2 # 공부
        },
        {
            'building' : 23, # 아루페관
            'purpose' : 3 # 팀플
        },
        {
            'building' : 23, # 아루페관
            'purpose' : 4 # 경로
        },
        {
            'building' : 23, # 아루페관
            'purpose' : 5 # 기타
        },
        {
            'building' : 24, # 체육관
            'purpose' : 1 # 휴게
        },
        {
            'building' : 24, # 체육관
            'purpose' : 4 # 경로
        },
        {
            'building' : 24, # 체육관
            'purpose' : 5 # 기타
        },
        {
            'building' : 25, # 베르크만스 우정원
            'purpose' : 1 # 휴게
        },
        {
            'building' : 25, # 베르크만스 우정원
            'purpose' : 2 # 공부
        },
        {
            'building' : 25, # 베르크만스 우정원
            'purpose' : 3 # 팀플
        },
        {
            'building' : 25, # 베르크만스 우정원
            'purpose' : 4 # 경로
        },
        {
            'building' : 25, # 베르크만스 우정원
            'purpose' : 5 # 기타
        }

            
            
            
    ]
    def handle(self, *args, **options):
        for building in self.Buildings:
            Building.objects.get_or_create(
                name = building['name'], 
                nickname = building['nickname'],
                latitude = building['latitude'],
                longitude = building['longitude']
            )
            
        for purpose in self.Purposes:
            Purpose.objects.get_or_create(
                name = purpose['name'],
                glyph = purpose['glyph']
            )
        
        for bp in self.BuidlingPurposes:
            BuildingPurpose.objects.get_or_create(
                building = Building.objects.get(id = bp['building']),
                purpose = Purpose.objects.get(id = bp['purpose'])
            )
                        
        self.stdout.write(self.style.SUCCESS('Buildings initialized'))
        return 0
            