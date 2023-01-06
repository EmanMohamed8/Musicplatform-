1. create some artists :

   python manage.py shell
   from artists import Artist
   object = (stageName = 'Eman', socialLink = 'Eman@gmail.com')
   object.save()
   object

2. list down all artists :

   Artist.object.all()
   <QuerySet [<Artist: Artist object (1)>, <Artist: Artist object (2)>, <Artist: Artist object (3)>]>

3. list down all sorted by name :

   Artist.objects.all().order_by('stageName')
   <QuerySet [<Artist: Artist object (3)>, <Artist: Artist object (2)>, <Artist: Artist object (1)>]>

4. list down all artists whose name starts with `a` :

   Artist.objects.all().filter(stageName\_\_startswith = 'a')
   <QuerySet [<Artist: Artist object (3)>]>

5. create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference) :

   from artists.models import Artist
   Tamer = Artist (stageName = 'Tamer')
   Tamer.save()
   from albums.models import Album
   Album1 = Album (album = Tamer, name = 'dream', cost = 700)
   Album1.save()

6. get the latest releaed album :

   Album.objects.latest('dateTime')
   <Album: Album object (2)>

7. get all albums released before today :

   from datetime import datetime, date, timedelta
   Album.objects.filter(dateTime\_\_lt=date.today())
   <QuerySet [<Album: Album object (3)>]>

   Album.objects.filter(dateTime\_\_gte=datetime.datetime.today()-datetime.timedelta(days=2))
   <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>

8. get all albums released today or before but not after today :

   Album.objects.filter(dateTime\_\_lte=date.today())
   <QuerySet [<Album: Album object (3)>]>

9. count the total number of albums (hint: count in an optimized manner) :

   Album.objects.all().count()
   3

10. for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference) :

    Artist.objects.all().values('album')  
    <QuerySet [{'album': None}, {'album': 3}, {'album': None}, {'album': 1}, {'album': 2}, {'album': None}]>

11. list down all albums ordered by cost then by name (cost has the higher priority) :

    Album.objects.order_by('name','cost')
    <QuerySet [<Album: Album object (3)>, <Album: Album object (1)>, <Album: Album object (2)>]>
