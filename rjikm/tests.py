from django.test import TestCase

# Create your tests here.
from .models import Editorinchief
# It creates an Editorinchief object with the given attributes.
class EditorinchiefTestCase(TestCase):
    def setUp(self):
        Editorinchief.objects.create(
            FullName='Tom', University='Technical University of Kenya', MyEmail='tom.kwanya@gmail.com'
        )


def test_str_method(self):
  """
  The function tests the str method of the Editorinchief model
  """
  editorinchief = Editorinchief.objects.get(pk=1)
  self.assertEqual(str(editorinchief),
                     'Tom Technical University of Kenya tom.kwanya@gmail.com')


def test_save_method(self):
  """
  It tests the save method of the Editorinchief model.
  """
  editorinchief = Editorinchief.objects.get(pk=1)
  self.assertEqual(editorinchief.FullName, 'Tom')
  self.assertEqual(editorinchief.University, 'Technical University of Kenya')
  self.assertEqual(editorinchief.MyEmail, 'tom.kwanya@gmail.com')
