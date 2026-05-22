from django.test import TestCase
from django.utils import timezone
from recipe.models import Category, Recipe


class CategoryModelTest(TestCase):
    """Test cases for Category model"""

    def setUp(self):
        """Create test category"""
        self.category = Category.objects.create(name="Italian")

    def test_category_creation(self):
        """Test that Category is created correctly"""
        self.assertEqual(self.category.name, "Italian")
        self.assertIsNotNone(self.category.id)

    def test_category_str_representation(self):
        """Test Category string representation"""
        self.assertEqual(str(self.category), "Italian")

    def test_category_name_unique(self):
        """Test that Category name is unique"""
        with self.assertRaises(Exception):
            Category.objects.create(name="Italian")

    def test_category_iter(self):
        """Test Category __iter__ method"""
        items = list(self.category)
        self.assertEqual(items, ["Italian"])

    def test_category_ordering(self):
        """Test that categories are ordered by name"""
        Category.objects.create(name="Asian")
        Category.objects.create(name="Mexican")
        
        categories = list(Category.objects.all())
        names = [cat.name for cat in categories]
        
        self.assertEqual(names, ["Asian", "Italian", "Mexican"])


class RecipeModelTest(TestCase):
    """Test cases for Recipe model"""

    def setUp(self):
        """Create test category and recipe"""
        self.category = Category.objects.create(name="Italian")
        self.recipe = Recipe.objects.create(
            title="Pasta Carbonara",
            description="Classic Italian pasta dish",
            instructions="Cook pasta, mix with eggs and bacon",
            ingredients="Pasta, eggs, bacon, cheese",
            category=self.category
        )

    def test_recipe_creation(self):
        """Test that Recipe is created correctly"""
        self.assertEqual(self.recipe.title, "Pasta Carbonara")
        self.assertEqual(self.recipe.category, self.category)
        self.assertIsNotNone(self.recipe.id)

    def test_recipe_str_representation(self):
        """Test Recipe string representation"""
        self.assertEqual(str(self.recipe), "Pasta Carbonara")

    def test_recipe_timestamps(self):
        """Test that created_at and updated_at are set"""
        self.assertIsNotNone(self.recipe.created_at)
        self.assertIsNotNone(self.recipe.updated_at)
        self.assertEqual(self.recipe.created_at, self.recipe.updated_at)

    def test_recipe_update(self):
        """Test that updated_at changes on update"""
        old_updated = self.recipe.updated_at
        self.recipe.title = "Updated Carbonara"
        self.recipe.save()
        
        self.assertGreaterEqual(self.recipe.updated_at, old_updated)

    def test_recipe_category_relationship(self):
        """Test Recipe-Category relationship"""
        recipes = self.category.recipes.all()
        self.assertEqual(recipes.count(), 1)
        self.assertIn(self.recipe, recipes)

    def test_recipe_ordering(self):
        """Test that recipes are ordered by created_at descending"""
        recipe2 = Recipe.objects.create(
            title="Risotto",
            description="Italian rice dish",
            instructions="Cook rice with broth",
            ingredients="Rice, broth, cheese",
            category=self.category
        )
        
        recipes = list(Recipe.objects.all())
        self.assertEqual(recipes[0].title, "Risotto")
        self.assertEqual(recipes[1].title, "Pasta Carbonara")

    def test_recipe_cascade_delete(self):
        """Test that recipes are deleted when category is deleted"""
        recipe_id = self.recipe.id
        self.category.delete()
        
        self.assertEqual(Recipe.objects.filter(id=recipe_id).count(), 0)

    def test_recipe_fields(self):
        """Test all recipe fields"""
        self.assertEqual(self.recipe.description, "Classic Italian pasta dish")
        self.assertEqual(self.recipe.instructions, "Cook pasta, mix with eggs and bacon")
        self.assertEqual(self.recipe.ingredients, "Pasta, eggs, bacon, cheese")

    def test_multiple_recipes_same_category(self):
        """Test multiple recipes with same category"""
        Recipe.objects.create(
            title="Pizza",
            description="Italian pizza",
            instructions="Prepare dough and toppings",
            ingredients="Dough, sauce, cheese",
            category=self.category
        )
        
        recipes = self.category.recipes.all()
        self.assertEqual(recipes.count(), 2)
