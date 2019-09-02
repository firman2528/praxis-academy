from kontener import Readers, Clients, Configs

if __name__ == "__main__" :
    Configs.config.override({
        "domain_name" : "imap.gmail.com",
        "email_address" : "firman.yuspriyadi@gmail.com",
        "password" : "firman25280720",
        "mailbox" : "INBOX"
    })
    email_reader = Readers.email_reader()
    print(email_reader.read('(SUBJECT TestSubject)'))