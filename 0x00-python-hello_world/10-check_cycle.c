#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the
 * linked list
 * @list: list to be checked
 * Return: 1 if there is a cycle and 0 if there is no
 * cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if(!list)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
