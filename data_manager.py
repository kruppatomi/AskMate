from datetime import datetime
import database_common


@database_common.connection_handler
def read_question_datas(cursor):
    cursor.execute("""SELECT * FROM question order by submission_time desc """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute("""select * from question where id = %(id)s""",
                   {'id': question_id})
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
    cursor.execute("""select * from answer where question_id = %(question_id)s order by submission_time desc""",
                   {'question_id': question_id})
    answ_datas = cursor.fetchall()
    return answ_datas



@database_common.connection_handler
def get_comment_by_question_id(cursor, question_id):
    cursor.execute("""select * from comment where question_id = %(question_id)s""",
                   {'question_id' : question_id})
    comm_datas = cursor.fetchall()
    return comm_datas


@database_common.connection_handler
def question_add(cursor, title, message):
    dt = datetime.now()
    cursor.execute("insert into question (submission_time, title, message) values(%(submission_time)s,"
                   "%(title)s, %(message)s)",
                   {'submission_time': dt,
                    'title': title,
                    'message': message})


@database_common.connection_handler
def get_newest_id(cursor):
    cursor.execute("select id from question order by id desc limit 1")
    return cursor.fetchall()


@database_common.connection_handler
def answer_add(cursor, message, question_id):
    dt = datetime.now()
    cursor.execute(
        "insert into answer (submission_time, question_id, message) values(%(submission_time)s, %(question_id)s,"
        "%(message)s)",
        {'submission_time': dt,
         'question_id': question_id,
         'message': message})


@database_common.connection_handler
def q_comment_add(cursor, message, question_id):
    dt = datetime.now()
    cursor.execute("insert into comment (submission_time, message, question_id) values(%(submission_time)s,"
                   "%(message)s,%(question_id)s)",
                {'submission_time': dt,
                  'message': message,
                 'question_id':question_id})


@database_common.connection_handler
def a_comment_add(cursor, message, question_id, answer_id):
    dt = datetime.now()
    cursor.execute("insert into comment (submission_time, message, question_id, answer_id) values(%(submission_time)s,"
                   "%(message)s,%(question_id)s,%(answer_id)s)",
                {'submission_time': dt,
                  'message': message,
                 'question_id':question_id,
                 'answer_id':answer_id})


@database_common.connection_handler
def edit_question(cursor, title, message, question_id):
    cursor.execute("update question set title = %(title)s, message = %(message)s where id = %(id)s",
                   dict(title=title, message=message, id=question_id))


@database_common.connection_handler
def get_answer_datas(cursor, answer_id):
    cursor.execute("select * from answer where id = %(id)s",
                   dict(id=answer_id))
    return cursor.fetchall()


@database_common.connection_handler
def get_comment_datas(cursor, comment_id):
    cursor.execute("select * from comment where id = %(id)s",
                   dict(id=comment_id))
    return cursor.fetchall()


@database_common.connection_handler
def edit_answer(cursor, message, answer_id):
    cursor.execute("update answer set message = %(message)s where id = %(id)s",
                   dict(message=message, id=answer_id))


@database_common.connection_handler
def search_question(cursor, search_phrase):
    cursor.execute("""SELECT * FROM question
                          WHERE title ILIKE %(search_phrase)s OR message ILIKE %(search_phrase)s;""",
                   {'search_phrase': '%' + search_phrase + '%'})
    search_result = cursor.fetchall()
    return search_result

@database_common.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""DELETE FROM question
                          WHERE id=%(id)s;""",
                   {'id': question_id})


@database_common.connection_handler
def edit_comment(cursor, message, comment_id):
    cursor.execute("update comment set message = %(message)s where id = %(id)s",
                   dict(message=message, id=comment_id))

@database_common.connection_handler
def delete_comment(cursor, comment_id):
    cursor.execute("delete from comment where id = %(id)s",
                   dict(id=comment_id))