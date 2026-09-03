# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ContentCalendar
import unittest
from datetime import date
from ContentCalendar import Channel, Author, Article, Status


class TestContentCalendar(unittest.TestCase):
    def setUp(self):
        self.channel = Channel(name="Tech", slug="tech")
        self.author = Author(name="Alice", email="alice@example.com")
        self.article = Article(title="Intro", channel=self.channel, author=self.author, deadline=date(2025, 12, 31), status=Status.DRAFT)

    def test_channel_creation(self):
        self.assertEqual(self.channel.name, "Tech")
        self.assertEqual(self.channel.slug, "tech")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Alice")
        self.assertEqual(self.author.email, "alice@example.com")

    def test_article_status(self):
        self.assertEqual(self.article.status, Status.DRAFT)

    def test_article_status_update(self):
        self.article.status = Status.PUBLISHED
        self.assertEqual(self.article.status, Status.PUBLISHED)

    def test_article_deadline(self):
        self.assertEqual(self.article.deadline, date(2025, 12, 31))

    def test_article_repr(self):
        self.assertIn("Intro", repr(self.article))

    def test_article_str(self):
        self.assertIn("Intro", str(self.article))

    def test_article_deadline_warning(self):
        self.assertFalse(self.article.is_overdue())

    def test_article_overdue(self):
        self.article.deadline = date(2020, 1, 1)
        self.assertTrue(self.article.is_overdue())

    def test_article_status_too_early(self):
        self.article.deadline = date(2020, 1, 1)
        self.article.status = Status.PUBLISHED
        self.assertTrue(self.article.is_too_early())

    def test_article_status_too_late(self):
        self.article.deadline = date(2025, 12, 31)
        self.article.status = Status.PUBLISHED
        self.assertFalse(self.article.is_too_late())

    def test_article_status_ok(self):
        self.article.deadline = date(2025, 12, 31)
        self.article.status = Status.PUBLISHED
        self.assertFalse(self.article.is_too_early())
        self.assertFalse(self.article.is_too_late())

    def test_article_is_published(self):
        self.article.status = Status.PUBLISHED
        self.assertTrue(self.article.is_published())

    def test_article_is_not_published(self):
        self.assertFalse(self.article.is_published())

    def test_article_is_published_or_draft(self):
        self.assertTrue(self.article.is_published_or_draft())
        self.article.status = Status.DRAFT
        self.assertTrue(self.article.is_published_or_draft())

    def test_channel_articles_count(self):
        self.channel.articles.append(self.article)
        self.assertEqual(self.channel.articles_count, 1)


if __name__ == "__main__":
    unittest.main()
