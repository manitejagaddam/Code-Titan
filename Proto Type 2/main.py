from core.orchestrator import Orchestrator




if __name__ == "__main__":
    application_name = input("Enter the application Name : ")
    application = Orchestrator()
    print("************************************************")
    print("1. Build Application")
    print("2. Build & Run Application")
    print("************************************************")
    option = int(input("Enter the option"))
    if(option == 1):
        application.build_app()
    elif(option == 2) :
        application.build_and_run()    