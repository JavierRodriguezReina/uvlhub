from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.modules.dashboard.forms import DashboardForm
from app.modules.dashboard import dashboard_bp
from app.modules.dataset.services import DataSetService
from app.modules.dataset.models import Author, DSMetaData

datasetservice = DataSetService()

'''
READ ALL
'''
@dashboard_bp.route('/dashboard', methods=['GET'])
@login_required
def index():
    form = DashboardForm()
    ndatasets = datasetservice.count_dsmetadata()
    nauthors = datasetservice.count_authors()

    # Formatear los datos para pasarlos a la plantilla

    #author_names = ["Juan", "Pedro", "Maria", "Ana"]
    #datasets_count = [2,3,4,7]

    author_names, dataset_counts = datasetservice.get_all_author_names_and_dataset_counts()

    # Ahora puedes usar `author_names` y `dataset_counts` por separado
    print("Author Names:", author_names)
    print("Dataset Counts:", dataset_counts)

    

    return render_template('dashboard/index.html', ndatasets=ndatasets, nauthors=nauthors, 
                           author_names=author_names, datasets_count=dataset_counts, form=form)
