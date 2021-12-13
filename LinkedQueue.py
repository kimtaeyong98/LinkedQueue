class LinkedQueue:

    class _Node:
        __slots__='_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._head._element#헤드값 리턴

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail=None
            return answer

    def enqueue(self,e):
        newest=self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next=newest

        self._tail = newest
        self._size +=1

    def rotate(self):#로테이션
        if self.is_empty():#큐가 비었는지 확인
            print("Queue is empty")
        else:
            self._tail._next = self._head #tail의 next를 head와 연결
            self._head=self._head._next #head값을 다음 노드로 변경
            self._tail=self._tail._next #tail값을 head로 변경
            self._tail._next=None #tail의 next를 끊기(마지막 노드)
                
    def display(self):#큐의 값을 출력
        if self.is_empty():#큐가 비었는지 확인
            print("Queue is empty")
        else:
            current = self._head#헤드 저장
            print("[",current._element,end='')#헤드 요소 출력
            while current._next:#헤드 이후 출력(노드가 가르키는게 없을때까지 반복)
                current = current._next
                print(",",current._element,end='')
            print(" ]")
            
       
LQ=LinkedQueue()#객체 생성

node =[1,3,5,7]#노드 값 저장 리스트

for data in node:#노드 추가
    LQ.enqueue(data)

print("Before Rotation: ",end='')
LQ.display()#로테이션 전 출력
LQ.rotate()#로테이션
print("After Rotation: ",end='')
LQ.display()#로테이션 후 출력

