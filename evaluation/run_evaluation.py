import asyncio

from main import assistant, session

from agents import Runner

from evaluation.test_cases import TEST_CASES

from evaluation.evaluator import evaluate_response


async def run_evaluation():

    passed = 0
    failed = 0

    print("=" * 60)
    print("             AI ASSISTANT EVALUATION")
    print("=" * 60)

    for test_case in TEST_CASES:

        print(
            f"\nTesting: {test_case['name']}"
        )

        try:

            result = await Runner.run(
                assistant,
                test_case["input"],
                session=session,
            )

            actual_response = str(
                result.final_output
            )

            passed_test = evaluate_response(
                test_case,
                actual_response,
            )

            if passed_test:

                print("PASS")

                passed += 1

            else:

                print("FAIL")

                print(
                    "Response:",
                    actual_response
                )

                failed += 1

        except Exception as e:

            print("ERROR")

            print(
                "Reason:",
                str(e)
            )

            failed += 1


    total = passed + failed

    print("\n" + "=" * 60)

    print(
        f"Passed: {passed}/{total}"
    )

    print(
        f"Failed: {failed}/{total}"
    )

    if total > 0:

        accuracy = (
            passed / total
        ) * 100

        print(
            f"Evaluation Score: {accuracy:.2f}%"
        )

    print("=" * 60)


if __name__ == "__main__":

    asyncio.run(
        run_evaluation()
    )