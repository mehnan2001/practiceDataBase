from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField()
    image = models.ImageField(upload_to='users/%Y/%m/%d/', default='users/default.jpg')
    description = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Post(models.Model):
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', default='blog/default.jpg')
    pubDate = models.DateTimeField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    viewCount = models.IntegerField(default=0)



    class Meta:
        ordering = ('-pubDate',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    userWebSite = models.URLField()
    comment = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=30)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
