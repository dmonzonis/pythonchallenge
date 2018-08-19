import xmlrpc.client


def main():
    # After some research we find out that the phonebook.php page listens for
    # XML-RPC requests
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    proxy = xmlrpc.client.ServerProxy(url)

    # Get a list of supported methods
    #  print(proxy.system.listMethods())

    # Find info about the phone method
    #  print(proxy.system.methodHelp('phone'))

    # Get the phone number of Bert (from last challenge's clue)
    print(proxy.phone('Bert'))
    # Prints 555-ITALY, try for italy.html, which is the solution to the challenge


if __name__ == "__main__":
    main()
