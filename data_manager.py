import connection
import util
from datetime import datetime
import time
import database_common

def get_current_time(format='%Y-%m-%d %H:%M:%S'):
    return datetime.utcfromtimestamp(time.time()).strftime(format)

@database_common.connection_handler
def read_datas(cursor):
    cursor.execute("""SELECT * FROM question order by submission_time desc """)
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute("""select * from question where id = %(id)s""",
                    {'id' : question_id})
    quest_datas = cursor.fetchall()
    return quest_datas
    '''questions = connection.read_datas()
    question_data = []
    for item in questions:
        item['id'] = int(item['id'])
        if question_id == item['id']:
            question_data.append(item)
    return question_data'''

@database_common.connection_handler
def get_answers_by_question_id(cursor, question_id):
    cursor.execute("""select * from answer where question_id = %(question_id)s""",
                   {'question_id' : question_id})
    answ_datas = cursor.fetchall()
    return answ_datas
    '''answers = connection.read_csv("answer.csv")
    answer_data = []
    for answer in answers:
        answer['question_id'] = int(answer['question_id'])
        if question_id == answer['question_id']:
            answer_data.append(answer)
    return answer_data'''


def question_add(title, message, image):
    question_added = {'id': util.get_next_id('question.csv'),
                      'submission_time': get_current_time(),
                      'view_number': 0,
                      'vote_number': 0,
                      'title': title,
                      'message': message,
                      'image': image,
                      }
    connection.add_question(question_added)
    return question_added


def answer_add(message, image, question_id):
    answer_added= {'id': util.get_next_id('answer.csv'),
                  'submission_time': get_current_time(),
                  'vote_number': 0,
                  'question_id': question_id,
                  'message': message,
                  'image': image}
    connection.add_answer(answer_added)
    return answer_added

def edit_question(title, message, id_, view_number=0, vote_number=0, image=""):
    edited_question = {'id': id_,
                       'submission_time': get_current_time(),
                       'title': title,
                       'message': message,
                       'view_number': view_number,
                       'vote_number': vote_number,
                       'image': image,
                       }
    connection.edit_question(edited_question)
    return edited_question
