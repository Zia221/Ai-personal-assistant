def evaluate_response(test_case, actual_response):

    actual_response = actual_response.lower()

    if "expected" in test_case:

        expected = test_case["expected"].lower()

        return expected in actual_response

    if "expected_contains" in test_case:

        expected = test_case["expected_contains"].lower()

        return expected in actual_response

    return False