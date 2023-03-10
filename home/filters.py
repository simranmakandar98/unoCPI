import django_filters
from projects.models import Project, EngagementType, ActivityType, Status, ProjectCampusPartner, \
    ProjectCommunityPartner, ProjectMission, ProjectSubCategory
from partners.models import CommunityPartner, CommunityPartnerMission, CampusPartner
from home.models import MissionArea
from django.db.models import Max, Min

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['engagement_type','academic_year','end_academic_year'  ]
    @property
    def qs(self):
        parent = super(ProjectFilter, self).qs
        return Project.objects.all()

class ProjectSubCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProjectSubCategory
        fields = ['sub_category', ]

class FromProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['engagement_type','academic_year','end_academic_year' ]


class ToProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['engagement_type','academic_year','end_academic_year' ]

class legislativeFilter(django_filters.FilterSet):

    legislative_district = django_filters.ModelChoiceFilter(queryset=Project.objects.values_list('legislative_district', flat=True).distinct())

    # legislative_district =   django_filters.NumberFilter('legislative_district')

    class Meta:
        model = Project
        fields = ['legislative_district',]



class ProjectMissionFilter(django_filters.FilterSet):
    class Meta:
        model = ProjectMission
        fields = ['mission', ]


class AcademicYearFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['academic_year', ]


class ProjectCampusFilter(django_filters.FilterSet):
    class Meta:
        model = ProjectCampusPartner
        fields = ['campus_partner', ]

class ProjectCommunityFilter(django_filters.FilterSet):
    class Meta:
        model = ProjectCommunityPartner
        fields = ['community_partner', ]


class communityPartnerFilter(django_filters.FilterSet):
    class Meta:
        model = CommunityPartner
        fields = ["weitz_cec_part", "community_type", "id"]


class CampusFilter(django_filters.FilterSet):
    class Meta:
        model = CampusPartner
        fields = ['name', 'college_name',]



class CommunityMissionFilter(django_filters.FilterSet):
    class Meta:
        model = CommunityPartnerMission
        fields = ["community_partner"]


class MissionAreaFilter(django_filters.FilterSet):
    class Meta:
        model = MissionArea
        fields = ["mission_name"]
