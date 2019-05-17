import questions
import random


def make_question(question, wrong_ans):
    current_ques = random.choice(list(question.keys()))
    correct = question[current_ques]
    options = [correct]
    while len(options) != 4:
        opt = random.choice(wrong_ans)
        if opt not in options:
            options.append(opt)
    return current_ques, correct, options


def process_data(question, wrong_ans, already_asked):
    each = 1

    while each == 1:
        current_ques, correct, options = make_question(question, wrong_ans)

        if current_ques not in already_asked:
            random.shuffle(options)
            obj = questions.Questions(current_ques, options, correct)
            already_asked.add(current_ques)

            print(obj.get_ques())
            print('1:', obj.get_ans1())
            print('2:', obj.get_ans2())
            print('3:', obj.get_ans3())
            print('4:', obj.get_ans4())

            return obj


def compare_answers(obj, player_score):
    answer = int(input('Enter your choice: '))
    if obj.correct_answer(answer):
        print('Correct Answer')
        player_score += 1
    else:
        print('Incorrect Answer')
    print('Score:', player_score)

    return player_score


def display_result(player_1, player_2):
    if player_1 > player_2:
        print('Congrats!! Player 1 won')
    elif player_1 < player_2:
        print('Congrats!! Player 2 won')
    else:
        print('It was a draw')


def players(question, wrong_ans):
    num = 0
    already_asked = set()
    player_1 = 0
    player_2 = 0
    while num < 10:
        if num % 2 == 0:
            print('Player 1:')

            obj1 = process_data(question, wrong_ans, already_asked)

            player_1 = compare_answers(obj1, player_1)

        else:
            print('Player 2:')
            obj2 = process_data(question, wrong_ans, already_asked)

            player_2 = compare_answers(obj2, player_2)

        print('\n')
        num += 1

    display_result(player_1, player_2)


def main():
    question = {'What are the names of the three good fairies from Sleeping Beauty?': 'Flora, Fauna, and Merryweather',
                'Who is the only Disney villain to never actually appear onscreen in their respective Disney film?': '“Man” from Bambi',
                'What are the names of the two eels who are Ursula’s sidekicks?': 'Flotsam and Jetsam',
                'Patrick Stewart has said that turning down this Disney character is the greatest regret of his film '
                'career.': 'Jafar',
                'What is the name of Mulan’s horse?': 'Khan',
                'Which Disney movie boasts the only soundtrack for an animated film to be certified Diamond (ten '
                'times platinum) '
                'by the Recording Industry Association of America?': 'The Lion King',
                'Which voice actor sang “Beauty and the Beast” from the 1991 animated film of the same name?': 'Angela Lansbury',
                'Which Disney movie’s soundtrack featured Mel Gibson?': 'Pocahontas',
                'What is the only Disney song to win a Grammy Award for Song of the Year?': 'A Whole New World',
                'How many Academy Awards for Best Original Songs has Disney won? (Hint: It’s less than 20.)': 'Twelve'}

    wrong_ans = ['Thumper in Bambi', 'Peter Pan in Peter Pan', 'Jiminy Cricket in Pinocchio', 'Fifteen',
                 'Jasmine in Aladdin',
                 '1993', 'Winifred, Mary, and Sarah', 'The Parent Trap',
                 'Pirates of the Caribbean: The Curse of the Black Pearl'
                 'Travis Coates']

    players(question, wrong_ans)


main()
