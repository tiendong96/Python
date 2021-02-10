browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
lastTab = browsing_session.pop()
print(lastTab)
print(browsing_session)
#browsing_session = true

if not browsing_session: #if browsing_session is not true
    print("No browsing history")
print("Last Tab", browsing_session[-1])    

# if not browsing_session:
#     print("redirect", browsing_session[-1]) #get item on top of the stack
# print("No browsing history.")

#false values: 0 "" not []

