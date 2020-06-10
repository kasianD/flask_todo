import functools

from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from app.forms import TaskForm
from app.models import Task
from .auth import login_required

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@bp.route('/', methods=['GET'])
@login_required
def list():
    tasks = Task.query.filter_by(user_id=session['user_id'], is_accomplished=False).order_by(Task.due_date).all()
    # tasks = Task.query.filter_by(user_id=session.get('user_id')).order_by(Task.due_date).all()
    finished_tasks = Task.query.filter_by(user_id=session['user_id'], is_accomplished=True).order_by(Task.due_date).all()
    return render_template('tasks_list.html', tasks=tasks, finished_tasks=finished_tasks)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TaskForm(request.form)
    if form.validate_on_submit():
        Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            is_accomplished=form.is_accomplished.data,
            user_id=session.get('user_id')
        ).create()
        return redirect(url_for('tasks.list'))
    return render_template('task_create.html', form=form)


@bp.route('/details/<int:id>', methods=['GET', 'POST'])
@login_required
def details(id):
    task = Task.query.get(id)
    form = TaskForm(request.form, obj=task)
    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(task)
            print(task)
            task.save()
            return redirect(url_for('tasks.list'))
    return render_template('task_details.html', form=form)


@bp.route('/done/<int:id>', methods=['GET'])
@login_required
def done(id):
    task = Task.query.get(id)
    task.is_accomplished = True
    task.save()

    return redirect(url_for('tasks.list'))


@bp.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):

    task = Task.query.get(id)
    task.delete()
    return redirect(url_for('tasks.list'))
