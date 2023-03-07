from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length=255
        )
    url = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        related_name='children',
        )
    
    def __str__(self):
        return self.title
    
    def children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []