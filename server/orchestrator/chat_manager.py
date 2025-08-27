from autogen import GroupChat, GroupChatManager

def create_chat_manager(agents):
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=12
    )
    return GroupChatManager(groupchat=groupchat, llm_config={"temperature": 0})
