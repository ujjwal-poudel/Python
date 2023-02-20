def Test(greeting):
    match greeting:
        case "hi":
            return "your language is like a child"
        case "hello":
            return "your language is like a teen"
        case "sup":
            return "your langugae is like a grown man"

Test("hello");
#why doesn't it works?
