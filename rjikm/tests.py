from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.
from .models import Editorinchief, Editorialboard, Article, Contact, Submit_article


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


def test_create_article_with_defaults(self):
  """
  The function creates an article object and then checks to see if the default values are set
  correctly
  """
  article = Article.objects.create()
  self.assertEqual(article.volume, "untitled")
  self.assertEqual(article.title, "Untitled")
  self.assertEqual(article.author1, "Anonymous")
  self.assertEqual(article.university1, "Unknown")
  self.assertEqual(article.department1, "Unknown")
  self.assertEqual(article.email1, "anonymous@example.com")
  self.assertEqual(article.author2, "Anonymous")
  self.assertEqual(article.department2, "Unknown")
  self.assertEqual(article.university2, "Unknown")
  self.assertEqual(article.email2, "anonymous@example.com")
  self.assertEqual(article.abstract_title, "Abstract")
  self.assertEqual(article.abstract, "No abstract provided")
  self.assertEqual(article.keyword_title, "Keyword")
  self.assertEqual(article.keywords, "None")


def test_create_article_with_non_defaults(self):
  """
  It creates an article with non-default values.
  """
  article = Article.objects.create(
      volume="Volume 1",
      title="My Article",
      author1="John Doe",
      university1="University of Example",
      department1="Department of Example",
      email1="john.doe@example.com",
      author2="Jane Doe",
      department2="Department of Example",
      university2="University of Example",
      email2="jane.doe@example.com",
      abstract_title="Abstract Title",
      abstract="This is the abstract of my article.",
      keyword_title="Keyword Title",
      keywords="keyword1, keyword2"
  )
  self.assertEqual(article.volume, "Volume 1")
  self.assertEqual(article.title, "My Article")
  self.assertEqual(article.author1, "John Doe")
  self.assertEqual(article.university1, "University of Example")
  self.assertEqual(article.department1, "Department of Example")
  self.assertEqual(article.email1, "john.doe@example.com")
  self.assertEqual(article.author2, "Jane Doe")
  self.assertEqual(article.department2, "Department of Example")
  self.assertEqual(article.university2, "University of Example")
  self.assertEqual(article.email2, "jane.doe@example.com")
  self.assertEqual(article.abstract_title, "Abstract Title")
  self.assertEqual(article.abstract, "This is the abstract of my article.")
  self.assertEqual(article.keyword_title, "Keyword Title")
  self.assertEqual(article.keywords, "keyword1, keyword2")



def test_create_contact_with_valid_values(self):
  """
  It creates a contact object with the given values.
  """
  contact = Contact.objects.create(
      name="John Doe",
      email="john.doe@example.com",
      message="This is a test message."
  )
  self.assertEqual(contact.name, "John Doe")
  self.assertEqual(contact.email, "john.doe@example.com")
  self.assertEqual(contact.message, "This is a test message.")


def test_create_contact_with_invalid_email(self):
  """
  This function will test the Contact model's create function by creating a Contact object with an
  invalid email address and then checking to see if a ValidationError is raised.
  """
  """
  using the Django TestCase class to create a test function that will test the Contact model's
  create function
  """
  with self.assertRaises(ValidationError):
      Contact.objects.create(
          name="John Doe",
          email="invalid-email",
          message="This is a test message."
      )

class SubmitArticleModelTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    file_content = b"Hello, World!"
    file = SimpleUploadedFile("test.txt", file_content)
    article = Submit_article.object.creat(
        title="Test Title",
        author="Test Author",
        university="Test University",
        email="test@example.com",
        abstract="Test abstract",
        keywords="Test keywords",
        doc_file=file
    )

    def test_delete(self):
      article = Submit_article.objects.get(title="Test Title")
      article.delete()
      self.assertFalse(article.doc_file, "The associated file was not deleted")
      
