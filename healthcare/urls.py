from django.urls import path
from .views import (PatientCreateView, PatientListView, PatientDetailView,DoctorListView,DoctorCreateView,DoctorDetailView,
                    MappingByPatientView,MappingCreateView,MappingListView,MappingDeleteView)

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', MappingListView.as_view(), name='mapping-list'),
    path('mappings/create/', MappingCreateView.as_view(), name='mapping-create'),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
