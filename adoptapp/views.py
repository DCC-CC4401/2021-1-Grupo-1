from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from posts.models import Post, PostImage, species
from django.db.models import Q
from users.models import Region


class HomepageView(View):

    def get(self, request):
        return render(request, "adoptapp/homepage.html")


def results_view(request):
    search = request.GET.get('q', '')
    query = Q(description__icontains=search) | Q(pet_name__icontains=search)
    filter_region = request.GET.get('filter-region', '')
    filter_specie = request.GET.get('filter-specie', '')
    filter_sex = request.GET.get('filter-sex', '')
    filter_size = request.GET.get('filter-size', '')
    filter_parasites = request.GET.get('filter-parasites', '')
    filter_sterilized = request.GET.get('filter-sterilized', '')
    filter_vaccinated = request.GET.get('filter-vaccinated', '')
    filter_status = request.GET.get('filter-status', '')
    filters = []
    filter_strs = []
    if filter_region:
        filters.append(Q(comuna__region_id=filter_region))
        filter_strs.append(Region.objects.get(id=filter_region).name)
    if filter_specie:
        filters.append(Q(specie=filter_specie))
        filter_strs.append(species['filter_specie'])
    if filter_sex:
        filters.append(Q(sex=filter_sex))
        filter_strs.append({'MA': 'Macho', 'HE': 'Hembra'}[filter_sex])
    if filter_size:
        filters.append(Q(pet_size=filter_size))
        filter_strs.append({'GR': 'Grande', 'ME': 'Mediano', 'PE': 'Pequeño'}[filter_size])
    if filter_parasites:
        filters.append(Q(parasytes=filter_parasites))
        filter_strs.append({'SI': 'Desparasitado', 'NO': 'No desparasitado'}[filter_parasites])
    if filter_sterilized:
        filters.append(Q(sterilized=filter_sterilized))
        filter_strs.append({'SI': 'Esterilizado', 'NO': 'No esterilizado'}[filter_sterilized])
    if filter_vaccinated:
        filters.append(Q(vaccinated=filter_vaccinated))
        filter_strs.append({'SI': 'Vacunado', 'NO': 'No vacunado'}[filter_vaccinated])
    if filter_status:
        filters.append(Q(status=filter_status))
        filter_strs.append({'Mío': 'Doméstico', 'Calle': 'Callejero'})
    print(filter_strs)
    results = Post.objects.filter(
        query,
        *filters)
    images = []
    for p in results:
        photo = PostImage.objects.filter(post_id=p.id).first()
        images.append(photo)
    results = list(zip(results, images))
    paginator = Paginator(results, 5)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)
    return render(request, "adoptapp/results.html", {'results': page_obj, 'filters': filter_strs})


class ResultsView(View):

    def get(self, request):
        return render(request, "adoptapp/results.html")