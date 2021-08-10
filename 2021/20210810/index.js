var app = new Vue({ 
    el: '#app',
    data: {
        message: '안녕 Vue!'
    }
});

// app.message = '이렇게하면 수정도 가능해요!'

var app2 = new Vue({
    el: '#app-2',
    data:{
        message: '이 페이지는 ' + new Date() + '에 로드 되었습니다.'
    }
})

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true
    }
})

var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            {text: 'JavaScript 배우기'},
            {text: 'Vue 배우기'},
            {text: '무언가 멋진 것을 만들기'}
        ]
    }
})
app4.todos.push({text: '이렇게도 추가 가능!'})

var app5 = new Vue({
    el: '#app-5',
    data:{
        message: '안녕하세요! Vue.js!'
    },
    methods:{
        reverseMessage: function(){
            this.message = this.message.split('').reverse().join('')
        }
    }
})

var app6 = new Vue({
    el: '#app-6',
    data: {
        message: '안녕하세요 Vue!'
    }
})

// 전역 컴포넌트
Vue.component('todo-item',{
    template: '<li>할일 항목 하나입니다.</li>'
})
var app7 = new Vue({
    el:'#app-7',
})

Vue.component('todo-item1', {
    props: ['todo'],
    template: '<li>{{todo.text}}</li>'
})
var app8 = new Vue({
    el: '#app-8',
    data: {
        groceryList:[
            {id: 0, text: '야채'},
            {id: 1, text: '치즈'},
            {id: 2, text: '고기'}
        ]
    }
})

var obj = { foo:'bar' }
Object.freeze(obj)
var app9 = new Vue({
    el: '#app-9',
    data: obj
})

/*
var app10 = new Vue({
    el: '#app-10',
    data: {
        firstName: 'Foo',
        lastName: 'Bar',
        fullName: 'Foo Bar'
    },
    watch: {
        firtName: function(val){
            this.fullName = val + ' ' + this.lastName
        },
        lastName: function(val){
            this.fullName = this.firstName + ' ' + val
        }
    }
})
*/
var app10 = new Vue({
    el: '#app-10',
    data: {
        firstName: 'Foo',
        lastName: 'Bar'
    },
    computed: {
        fullName: function(){
            return this.firstName + ' ' + this.lastName
        }
    }
})
/*
get과 set을 이용하려면 아래와 같이 사용하면 된다.
  computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}  
*/

var app11 = new Vue({
    el: '#app-11',
    data: {
        question: '',
        answer: '질문을 하기 전까지는 대답할 수 없습니다.'
    },
    watch: {
        // 질문이 변경될 때 마다 이 기능이 실행됩니다.
        question: function (newQuestion) {
          this.answer = '입력을 기다리는 중...'
          this.debouncedGetAnswer()
        }
      },
      created: function () {
        // _.debounce는 lodash가 제공하는 기능으로
        // 특히 시간이 많이 소요되는 작업을 실행할 수 있는 빈도를 제한합니다.
        // 이 경우, 우리는 yesno.wtf/api 에 액세스 하는 빈도를 제한하고,
        // 사용자가 ajax요청을 하기 전에 타이핑을 완전히 마칠 때까지 기다리길 바랍니다.
        // _.debounce 함수(또는 이와 유사한 _.throttle)에 대한
        // 자세한 내용을 보려면 https://lodash.com/docs#debounce 를 방문하세요.
        this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
      },
      methods: {
        getAnswer: function () {
          if (this.question.indexOf('?') === -1) {
            this.answer = '질문에는 일반적으로 물음표가 포함 됩니다. ;-)'
            return
          }
          this.answer = '생각중...'
          var vm = this
          axios.get('https://yesno.wtf/api')
            .then(function (response) {
              vm.answer = _.capitalize(response.data.answer)
            })
            .catch(function (error) {
              vm.answer = '에러! API 요청에 오류가 있습니다. ' + error
            })
        }
      }
    })

var app12 = new Vue({
    el: '#app-12',
    data:{
        asesome: false
    }
})

var app13 = new Vue({
    el: '#app-13'
})

var app14 = new Vue({
    el: '#app-14',
    data:{
        type: 'Z'
    }
})

var app15 = new Vue({
    el: '#app-15',
    data:{
        loginType: 'username'
    }
})

var app16 = new Vue({
    el: '#app-16',
    data:{
        ok: true    
    }
})

var app17 = new Vue({
    el: '#app-17',
    data:{
        items: [
            {message: 'Foo'},
            {message: 'Bar'}
        ]
    }
})

var app18 = new Vue({
    el: '#app-18',
    data:{
        parentMessage: 'Parent',
        items: [
            {message: 'Foo'},
            {message: 'Bar'}
        ]
    }
})

var app19 = new Vue({
    el: '#app-19',
    data:{
        object:{
            title: '제목',
            author: '저자',
            publishedAt: '2021-08-10'
        }
    }
})

var app20 = new Vue({
    el: '#app-20',
    data:{
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    methods:{
        even: function(numbers){
            return this.numbers.filter(function(n){
                return n % 2 === 0
            })
        }
    }
})

var app21 = new Vue({
    el: '#app-21'
})

Vue.component('todo-item', {
    template: '\
        <li>\
        {{ title }}\
        <button v-on:click="$emit(\'remove\')">Remove</button>\
        </li>\
    ',
    props: ['title']
    })      
var app22 = new Vue({
    el: '#app-22',
    data: {
        newTodoText: '',
        todos: [
            {
                id: 1,
                title: 'Do the dishes',
            },
            {
                id: 2,
                title: 'Take out the trash',
            },
            {
                id: 3,
                title: 'Mow the lawn'
            }
        ],
        nextTodoId: 4
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
                id: this.nextTodoId++,
                title: this.newTodoText
            })
            this.newTodoText = ''
        }
    }
})

var app23 = new Vue({
    el: '#app-23',
    data:{
        counter: 0
    }
})

var app24 = new Vue({
    el: '#app-24',
    data:{
        name: 'Vue.js'
    },
    methods: {
        greet: function (event) {
          // 메소드 안에서 사용하는 `this` 는 Vue 인스턴스를 가리킵니다
          // alert('Hello ' + this.name + '!')
          // `event` 는 네이티브 DOM 이벤트입니다
          if (event) {
            alert(event.target.tagName)
          }
        }
    }
})
app24.greet()

var app25 = new Vue({
    el: '#app-25',
    methods:{
        say: function(message){
            alert(message)
        },
        warn: function(message, event){
            if(event) {
                event.preventDefault()
            }
            alert(message)
        }
    }
})