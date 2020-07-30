from blog import models as model_blog
# from gallery import models as model_galleries

def blog_categories(request):
    return {
        'blog_categories': model_blog.Category.objects.all()
    }

# def gallery_photo_categories(request):
#     return {
#         'gallery_photo_categories' : model_galleries.Category.objects.filter(type__type_desc='photo')
#     }
