#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list to check
 *
 * Return: 1 if has a cycle in it or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL   && check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
