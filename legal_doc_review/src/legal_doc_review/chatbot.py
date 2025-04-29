# # import os
# # from tools.document_loader_tool import DocumentLoaderTool
# # from legal_doc_review.tools.ai_contract_updater import AIContractUpdater

# # # from tools.contract_updater_tool import ContractUpdaterTool
# # # from tools.contract_updater_tool import ContractUpdaterTool

# # def run_cli_chatbot():
# #     print("\n⚖️ Welcome to the Legal Contract Update Assistant (CLI Version)\n")

# #     # Step 1: Ask for file name only
# #     filename = input("📄 Enter the file name (e.g. contract.txt): ").strip()
# #     # file_path = os.path.join("samples", filename)
# #     file_path = os.path.join(os.path.dirname(__file__), 'samples', filename)

# #     print(f"🔍 Looking for file: {file_path}")

# #     if not os.path.exists(file_path):
# #         print(f"❌ Error: File '{file_path}' not found. Please check the 'samples/' folder.")
# #         return

# #     # Step 2: Load contract
# #     loader = DocumentLoaderTool()
# #     contract_text = loader._run(file_path=file_path)

# #     if not contract_text.strip():
# #         print("❌ Error: Contract is empty!")
# #         return

# #     print("\n✅ Contract loaded successfully!")
# #     print("\n💬 You can now make up to 5 contract update requests (type natural language)\n")

# #     updater = AIContractUpdater(model="llama3.2")
# #     question_count = 0

# #     while question_count < 5:
# #         user_input = input(f"🧑 Your request ({5 - question_count} left): ").strip()

# #         if not user_input:
# #             print("⚠️ Please enter a valid instruction.")
# #             continue

# #         # reply, updated_contract_text = updater.process_user_query(user_input, contract_text)
# #         updated_contract_text = updater.rewrite_contract(contract_text, user_input)


# #         print(f"\n🤖 Bot: {reply}")

# #         # Only update if it's a valid update
# #         if "couldn't understand" not in reply.lower():
# #             contract_text = updated_contract_text
# #             question_count += 1
# #         else:
# #             print("❌ Could not apply this update. Try asking differently.")

# #     # Step 3: Save updated contract
# #     os.makedirs('outputs', exist_ok=True)
# #     output_path = os.path.join("outputs", f"updated_contract_{filename}")
# #     with open(output_path, 'w', encoding='utf-8') as f:
# #         f.write(contract_text)

# #     print(f"\n✅ Final updated contract saved at: {output_path}")

# # if __name__ == "__main__":
# #     run_cli_chatbot()



# import os
# from tools.document_loader_tool import DocumentLoaderTool
# from tools.ai_contract_updater import AIContractUpdater

# def run_cli_chatbot():
#     print("\n⚖️ Welcome to the Legal Contract Update Assistant (CLI Version)\n")

#     # Step 1: Ask for file name only
#     filename = input("📄 Enter the file name (e.g. contract.txt): ").strip()
#     file_path = os.path.join(os.path.dirname(__file__), 'samples', filename)


#     print(f"🔍 Looking for file: {file_path}")

#     if not os.path.exists(file_path):
#         print(f"❌ Error: File '{file_path}' not found. Please check the 'samples/' folder.")
#         return

#     # Step 2: Load contract
#     loader = DocumentLoaderTool()
#     contract_text = loader._run(file_path=file_path)

#     if not contract_text.strip():
#         print("❌ Error: Contract is empty!")
#         return

#     print("\n✅ Contract loaded successfully!")
#     print("\n💬 You can now make up to 5 contract update requests (type natural language)\n")

#     updater = AIContractUpdater(model="llama3.2")  # use "llama3" or "mistral" or whatever you pulled
#     question_count = 0

#     while question_count < 5:
#         user_input = input(f"🧑 Your request ({5 - question_count} left): ").strip()

#         if not user_input:
#             print("⚠️ Please enter a valid instruction.")
#             continue

#         try:
#             updated_contract_text = updater.rewrite_contract(contract_text, user_input)
#             reply = "✅ Contract updated based on your request."
#         except Exception as e:
#             reply = f"❌ Error during update: {str(e)}"
#             updated_contract_text = contract_text

#         print(f"\n🤖 Bot: {reply}")

#         # Only update if not error
#         if "❌" not in reply:
#             contract_text = updated_contract_text
#             question_count += 1
#         else:
#             print("⚠️ Try phrasing your request differently.")

#     # Step 3: Save updated contract
#     os.makedirs('outputs', exist_ok=True)
#     output_path = os.path.join("outputs", f"updated_contract_{filename}")
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write(contract_text)

#     print(f"\n✅ Final updated contract saved at: {output_path}")

# if __name__ == "__main__":
#     run_cli_chatbot()




# import os
# from tools.document_loader_tool import DocumentLoaderTool
# from tools.ai_contract_updater import AIContractUpdater

# def run_cli_chatbot():
#     print("\n⚖️ Welcome to the Legal Contract Update Assistant (CLI Version)\n")

#     # Step 1: Ask for file name only
#     filename = input("📄 Enter the file name (e.g. contract.txt): ").strip()
#     file_path = os.path.join(os.path.dirname(__file__), 'samples', filename)

#     print(f"🔍 Looking for file: {file_path}")

#     if not os.path.exists(file_path):
#         print(f"❌ Error: File '{file_path}' not found. Please check the 'samples/' folder.")
#         return

#     # Step 2: Load contract
#     loader = DocumentLoaderTool()
#     contract_text = loader._run(file_path=file_path)

#     if not contract_text.strip():
#         print("❌ Error: Contract is empty!")
#         return

#     print("\n✅ Contract loaded successfully!")
#     print("\n💬 You can now make up to 5 contract update requests (type natural language)\n")

#     updater = AIContractUpdater(model="llama3")  # use "llama3" or "mistral" or whatever you pulled
#     question_count = 0

#     while question_count < 5:
#         user_input = input(f"🧑 Your request ({5 - question_count} left): ").strip()

#         if not user_input:
#             print("⚠️ Please enter a valid instruction.")
#             continue

#         try:
#             updated_contract_text = updater.rewrite_contract(contract_text, user_input)
#             reply = "✅ Contract updated based on your request."
#         except Exception as e:
#             reply = f"❌ Error during update: {str(e)}"
#             updated_contract_text = contract_text

#         print(f"\n🤖 Bot: {reply}")

#         # Only update if not error
#         if "❌" not in reply:
#             contract_text = updated_contract_text
#             question_count += 1
#         else:
#             print("⚠️ Try phrasing your request differently.")

#     # Step 3: Save updated contract
#     os.makedirs('outputs', exist_ok=True)
#     output_path = os.path.join("outputs", f"updated_contract_{filename}")
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write(contract_text)

#     print(f"\n✅ Final updated contract saved at: {output_path}")

# if __name__ == "__main__":
#     run_cli_chatbot()




import os
from tools.document_loader_tool import DocumentLoaderTool
from tools.ai_contract_updater import AIContractUpdater

def run_cli_chatbot():
    print("\n⚖️ Welcome to the Legal Contract Update Assistant (CLI Version)\n")

    # Step 1: Ask for file name only
    filename = input("📄 Enter the file name (e.g. contract.txt): ").strip()
    file_path = os.path.join(os.path.dirname(__file__), 'samples', filename)

    print(f"🔍 Looking for file: {file_path}")

    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found. Please check the 'samples/' folder.")
        return

    # Step 2: Load contract
    loader = DocumentLoaderTool()
    contract_text = loader._run(file_path=file_path)

    if not contract_text.strip():
        print("❌ Error: Contract is empty!")
        return

    print("\n✅ Contract loaded successfully!")
    print("\n💬 You can now make up to 5 contract update requests (type natural language)")
    print("📌 Type 'exit' or press Enter 'q' anytime to finish early.\n")

    updater = AIContractUpdater(model="llama3.2")
    question_count = 0
    MAX_QUESTIONS = 5
    
    while question_count < MAX_QUESTIONS:
        user_input = input(f"🧑 Your request ({MAX_QUESTIONS - question_count} left): ").strip()

        if user_input.lower() in {"exit", "quit", "q", ""}:
            print("\n👋 Exiting update loop early.")
            break

        try:
            updated_contract_text = updater.rewrite_contract(contract_text, user_input)

            if updated_contract_text.strip().startswith("❌"):
                reply = updated_contract_text  # Show rejection from updater
                print(f"\n🤖 Bot: {reply}")
                print("⚠️ That request wasn't relevant to the current contract.")
                continue  # Don't count this toward question count
            else:
                reply = "✅ Contract updated based on your request."
                contract_text = updated_contract_text
                question_count += 1

        except Exception as e:
            reply = f"❌ Error during update: {str(e)}"
            print(f"\n🤖 Bot: {reply}")
            continue

        print(f"\n🤖 Bot: {reply}")


    # while question_count < MAX_QUESTIONS:
    #     user_input = input(f"🧑 Your request ({MAX_QUESTIONS - question_count} left): ").strip()

    #     # Early exit if user types exit or leaves blank
    #     if user_input.lower() in {"exit", "quit", "q"}:
    #         print("\n👋 Exiting update loop early.")
    #         break

    #     try:
    #         updated_contract_text = updater.rewrite_contract(contract_text, user_input)
    #         reply = "✅ Contract updated based on your request."
    #     except Exception as e:
    #         reply = f"❌ Error during update: {str(e)}"
    #         updated_contract_text = contract_text

    #     print(f"\n🤖 Bot: {reply}")

    #     if "❌" not in reply:
    #         contract_text = updated_contract_text
    #         question_count += 1
    #     else:
    #         print("⚠️ Try phrasing your request differently.")

    # Step 3: Save updated contract
    os.makedirs('outputs', exist_ok=True)
    output_path = os.path.join("outputs", f"updated_contract_{filename}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contract_text)

    print(f"\n✅ Final updated contract saved at: {output_path}")

if __name__ == "__main__":
    run_cli_chatbot()
