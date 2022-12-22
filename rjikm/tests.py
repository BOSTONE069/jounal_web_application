from django.test import TestCase

# Create your tests here.
from .models import Editorinchief, Editorialboard
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


def test_str_method2(self):
  """
  The function tests whether the Editorialboard model's __str__ method returns the correct string
  """
  editorialboard = Editorialboard.objects.get(pk=1)
  self.assertEqual(str(editorialboard), 'Prof Tom Kwanya Technical University of Kenya Kenya')


def test_save_method2(self):
  """
  It tests whether the save method of the Editorialboard model works as expected.
  """
  editorialboard = Editorialboard.objects.get(pk=1)
  self.assertEqual(editorialboard.Prefix, 'Prof')
  self.assertEqual(editorialboard.FirstName, 'Tom')
  self.assertEqual(editorialboard.SecondName, 'Kwanya')
  self.assertEqual(editorialboard.University,
                     'Technical University of Kenya')
  self.assertEqual(editorialboard.Country, 'Kenya')


def test_get_method(self):
  """
  It tests the get method of the Editorialboard model.
  """
  editorialboard = Editorialboard.objects.get(pk=1)
  self.assertEqual(editorialboard.Prefix, 'Prof')
  self.assertEqual(editorialboard.FirstName, 'Tom')
  self.assertEqual(editorialboard.SecondName, 'Kwanya')
  self.assertEqual(editorialboard.University,
                     'Technical University of Kenya')
  self.assertEqual(editorialboard.Country, 'Kenya')
