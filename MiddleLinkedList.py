class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp=head
        temp1=head
        c=0
        m=0
        while(temp!=None):
            c+=1
            temp=temp.next
        k=c//2+1

        while(temp1!=None):
            m+=1
            if m==k:
                return temp1
            temp1=temp1.next
            
