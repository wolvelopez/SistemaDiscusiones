#Vamos a traer la foto de del perfil de Facebook o twitter
def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):

    url = None
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/%s/picture?type=large'%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        print "La URL de la imagen es: " + url
        user.avatar = url
        user.save()