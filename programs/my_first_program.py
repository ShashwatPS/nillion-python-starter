from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    A = SecretInteger(Input(name="A", party=party1))
    B = SecretInteger(Input(name="B", party=party1))
    C = SecretInteger(Input(name="C", party=party1))
    my_array_1 = Array(SecretInteger(Input(name="my_array_1", party=party1)), size=5)

    D = SecretInteger(Input(name="D", party=party2))
    E = SecretInteger(Input(name="E", party=party2))
    F = SecretInteger(Input(name="F", party=party2))
    my_array_2 = Array(SecretInteger(Input(name="my_array_2", party=party2)), size=5)

    G = SecretInteger(Input(name="G", party=party3))
    H = SecretInteger(Input(name="H", party=party3))
    I = SecretInteger(Input(name="I", party=party3))
    my_array_3 = Array(SecretInteger(Input(name="my_array_3", party=party3)), size=5)

    @nada_fn
    def multiply_and_add(a: SecretInteger, b: SecretInteger, c: SecretInteger) -> SecretInteger:
        return (a * b) + c

    @nada_fn
    def inc_array_element(a: SecretInteger) -> SecretInteger:
        return a + C

    @nada_fn
    def conditional_operation(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return a if a > b else b

    new_array_1 = my_array_1.map(inc_array_element)
    new_array_2 = my_array_2.map(inc_array_element)
    new_array_3 = my_array_3.map(inc_array_element)

    combined_tuple_array = Array.new(A, B, D, E, G, H)

    TMP1 = multiply_and_add(A, B, C)
    TMP2 = multiply_and_add(D, E, F)
    TMP3 = multiply_and_add(G, H, I)

    INTERMEDIATE1 = TMP1 + TMP2
    INTERMEDIATE2 = TMP2 * TMP3

    CONDITIONAL_RESULT = conditional_operation(INTERMEDIATE1, INTERMEDIATE2)

    FINAL_RESULT = INTERMEDIATE1 + INTERMEDIATE2 + CONDITIONAL_RESULT

    output1 = Output(new_array_1, "output_array_1", party1)
    output2 = Output(new_array_2, "output_array_2", party2)
    output3 = Output(new_array_3, "output_array_3", party3)
    output4 = Output(combined_tuple_array, "combined_tuple_array", party1)
    output5 = Output(FINAL_RESULT, "final_result", party2)
    output6 = Output(CONDITIONAL_RESULT, "conditional_result", party3)

    return [output1, output2, output3, output4, output5, output6]
