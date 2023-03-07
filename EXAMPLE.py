def friendly_reminder(func):
    func()
    print('Don\'t forget to bring your wallet!')
@friendly_reminder
def action():
    print('I am going to the store buy you something nice.')