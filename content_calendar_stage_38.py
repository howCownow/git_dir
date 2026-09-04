# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ContentCalendar
def test_edge_cases():
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", status="draft", author="a", channel="ch")
    assert ContentCalendar().publish(content="hi", deadline="2025-13-01") is None
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", status="draft") is None
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", author="a", channel="ch") is None
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", status="draft", channel="ch") is None
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", status="draft", author="a") is None
    assert ContentCalendar().publish(content="hi", deadline="2025-01-01", status="draft", author="a", channel="ch", extra="x")
    cal = ContentCalendar()
    cal.publish(content="ok", deadline="2025-01-01", status="draft", author="a", channel="ch")
    assert len(cal) == 1
    assert cal[0].content == "ok"
    assert cal[0].deadline == "2025-01-01"
    assert cal[0].status == "draft"
    assert cal[0].author == "a"
    assert cal[0].channel == "ch"
    cal.publish(content="ok", deadline="2025-01-01", status="draft", author="a", channel="ch")
    assert len(cal) == 1
    assert cal[0].content == "ok"
    assert cal[0].deadline == "2025-01-01"
    assert cal[0].status == "draft"
    assert cal[0].author == "a"
    assert cal[0].channel == "ch"
    cal.publish(content="ok", deadline="2025-01-01", status="draft", author="a", channel="ch")
    assert len(cal) == 1
    assert cal[0].content == "ok"
    assert cal[0].deadline == "2025-01-01"
    assert cal[0].status == "draft"
    assert cal[0].author == "a"
    assert cal[0].channel == "ch"
